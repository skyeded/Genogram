import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import Papa from 'papaparse';

import './newData.css';

export function createData(name, size, uploadedBy, date, file) {
  return { name, size, uploadedBy, date, file };
}

function NewData() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);
  const [filePreview, setFilePreview] = useState(null);

  const upload = () => {
    if (!file) {
      console.error('File is empty or null.');
      return;
    }
  
    const formData = new FormData();
    formData.append('data', file);
  
    // Send the FormData object to the server
    axios.post('http://localhost:3005/ML_data', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
      .then((res) => {
        console.log(res.data);
        setError(null);
  
        toast.success('Successfully Uploaded', {
          position: toast.POSITION.TOP_CENTER,
        });
      })
      .catch((err) => {
        console.error('Error:', err.message);
        setError('An error occurred. Please try again.');
      });
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];

    if (selectedFile) {
      setFile(selectedFile);
      setError(null);

      const reader = new FileReader();
      reader.onload = (event) => {
        setFilePreview(event.target.result);
      };
      reader.readAsText(selectedFile);
    }
  };

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: '100vh', // Take full viewport height
    }}>
      <div className="AddData" style={{ marginBottom: '40px', borderRadius: '10px', padding: '5px 20px' }}>
        <a style={{ fontSize: '25px', color: 'black', padding: '20px 10px', letterSpacing: '2px', textShadow: '5px 5px 15px' }}>Add new Data!</a>
      </div>
      <div style={{ display: 'flex', marginRight: '10px' }}>
        <input type="file" onChange={handleFileChange} component="label" variant="contained" style={{ marginRight: '-50px' }} />
        <Button onClick={upload} component="label" variant="contained" startIcon={<CloudUploadIcon />} style={{ marginTop: '-10px' }}>
          Upload file
        </Button>
      </div>

      {filePreview && (
        <div style={{ marginTop: '20px', overflowX: 'auto' }}>
          <h4>File Preview:</h4>
          <pre>{filePreview}</pre>
        </div>
      )}

      {file && (
        <div style={{ marginTop: '10px' }}>
          <h4>Selected File Details:</h4>
          <p>File Name: {file.name}</p>
          <p>File Size: {file.size} bytes</p>
          {error && <div style={{ color: 'red', marginTop: '10px' }}>{error}</div>}
        </div>
      )}

      <ToastContainer />
    </div>
  );
}

export default NewData;
