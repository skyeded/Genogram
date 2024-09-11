const express = require('express');
const cors = require('cors');
const { Client } = require('pg');
const { from } = require('pg-copy-streams');
const multer = require('multer');
const fs = require('fs')
const fsp = fs.promises
const { pipeline } = require('node:stream/promises')
const { Readable } = require('stream');
const { table } = require('console');

const app = express()
app.use(cors())
app.use(express.json());

const storage = multer.diskStorage({
    destination: function(req, file, cb) {
        return cb(null, "./public/Images")
    },
    filename: function(req, file, cb) {
        return cb (null, `${Date.now()}_${file.originalname}`)
    }
})

const upload = multer({storage})

const client = new Client({
    host: "localhost",
    user: "postgres",
    port: 5432,
    password: "129303",
    database: "NewDB"
})

app.post('/upload', upload.single('file'), async (req, res) => {
    try {

        console.log(req.body);
        console.log(req.file);

        // Proceed with inserting data into the database
        // ...

        // Read the file content
        const filePath = req.file.path;
        const fileContent = await fsp.readFile(filePath, 'utf8');

        // Fetch column names from the PostgreSQL table
        const { rows: tableColumns } = await client.query("SELECT column_name FROM information_schema.columns WHERE table_name = 'newtable'");

        // Extract column headers from the first line of the CSV file
        const csvHeaders = fileContent.split('\n')[0].split(',').map(header => header.trim());
        console.log('Column names of the uploaded file:', csvHeaders);

        // Split the file content into lines
        const lines = fileContent.split('\n');

        // Extract and process the remaining rows
        const csvRows = lines.slice(1).map(row => {
            // Split each row into columns
            const columns = row.split(',').map(header => header.trim());

            // Quote fields to handle special characters
            const quotedColumns = columns.map(column => `"${column}"`);

            // Join the columns back into a row
            return quotedColumns.join(',');
        });

        // Check for duplicates in the nid column
        const nidIndex = csvHeaders.indexOf('nid');
        const uniqueNids = new Set();
        const uniqueCsvRows = csvRows.map(row => {
            const columns = row.split(',');
            const nid = columns[nidIndex];
            const isDuplicate = uniqueNids.has(nid);
            if (isDuplicate) {
                // Change nid to a unique ID (you can implement your logic here)
                columns[nidIndex] = generateUniqueID(); // Replace with your logic
            }
            uniqueNids.add(columns[nidIndex]);
            return columns.join(',');
        });

        // Transform text file data into CSV format (each line becomes a row)
        const csvContent = [csvHeaders.join(','), ...uniqueCsvRows].join('\n');

        const excludedColumns = ['fam_id', 'isEdit'];

        const missingColumns = tableColumns
          .filter(column => !excludedColumns.includes(column.column_name)) // Exclude specified columns
          .filter(column => !csvHeaders.includes(column.column_name));

        console.log('Missing columns (except fam_id and isEdit):', missingColumns.map(column => column.column_name));

        if (missingColumns.length > 0) {
          const errorMessage = `Missing columns (except fam_id and isEdit): ${missingColumns.map(column => column.column_name).join(', ')}`;
          console.log(errorMessage);
          return res.status(400).json({ error: errorMessage });
        }

        console.log('CSV Content:', csvContent);
        const ingestStream = client.query(from('COPY newtable(is_hh_head,is_fam_head,title,sex,hh_id,fam_id,nid,fa_nid,mo_nid,name,surname,fa_name,mo_name,fa_surname,mo_surname,birthyear,isEdit) FROM STDIN WITH (FORMAT CSV, HEADER true)'));

        const sourceStream = new Readable();
        sourceStream.push(csvContent);
        sourceStream.push(null);
            
        // Use pipeline to handle the stream
        await pipeline(sourceStream, ingestStream);
            
        // Remove the file after insertion
        await fsp.unlink(filePath);

        if (!req.file) {
            return res.status(400).json({ error: 'No file uploaded' });
        }

        return res.status(200).json({ message: 'File uploaded successfully' });
    } catch (error) {
        console.error(error);
        return res.status(500).json({ error: 'Internal server error' });
    }
});

client.connect();

client.query('Select * from newtable', (err, res)=>{
    if(!err){
        console.log(res.rows);
    } else {
        console.log(err.message);
    }
    client.end;
})

app.listen(3001, () => {
    console.log("server is running!")
})