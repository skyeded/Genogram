import React, { useState } from 'react';

// Import createData from NewData (assuming it's exported from there)
import { createData } from 'C:/Users/User/Desktop/CS400/client/src/addNewData/newData.js'; // Replace '../path-to/NewData' with the correct path

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const HistoryTable = () => {
  // Use the same initial rows state as in NewData
  const [rows, setRows] = useState([
    createData('File1.txt', '101', 'Arnuparp', '2023-09-10', 'To DB'),
    createData('File2.pdf', '102', 'Mark', '2023-08-22', 'To DB'),
    createData('File2.pdf', '103', 'Theerawuth', '2023-08-18', 'To DB'),
    createData('File2.pdf', '104', 'Ryu', '2023-08-12', 'To DB'),
    createData('File2.pdf', '105', 'Gyu', '2023-07-29', 'To DB')
    // Add more rows as needed
  ]);

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="file history table">
        <TableHead>
          <TableRow>
            <TableCell align="right">Family ID</TableCell>
            <TableCell align="right">Edited By</TableCell>
            <TableCell align="right">Date</TableCell>
            <TableCell align="right">Database</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">{row.size}</TableCell>
              <TableCell align="right">{row.uploadedBy}</TableCell>
              <TableCell align="right">{row.date}</TableCell>
              <TableCell align="right">
                <a href={row.file} download>
                  To DB
                </a>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default HistoryTable;
