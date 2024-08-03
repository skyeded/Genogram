import React from 'react';
import { Link } from 'react-router-dom';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import { green } from '@mui/material/colors';
import TextField from '@mui/material/TextField';

import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

import Button from '@mui/material/Button';


import './Search.css';

const Search = () => {

    const [filter, setFilter] = React.useState('');

    const handleChange = (event) => {
    setFilter(event.target.value);
    };
    
  return (
    <div className="searchBody">
        <ul>
            <li className="outer">
                Search!
            </li>
            <li className="outer">
                Type in any famID you want to see!
            </li>
            <li>
                <div className="searchBar">
                    <ul>
                        <li className="bar">
                            <TextField id="search" label="Search" variant="standard"  
                            sx={{
                                width: '200px', // Example width, adjust as needed
                                height: '50px',
                                borderColor: '#618264',
                                color:"#618264",
                                '&.active': {
                                    color: '#618264',
                                    borderColor: '#618264'
                                }
                              }}/>
                        </li>
                        <li className="">
                        <Box sx={{ width: '100px', height: '40px', marginTop: '10px'}}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label" sx={{marginTop: '-7px', color: 'success'}}>Filter</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={filter}
          onChange={handleChange}
          label="Filter"
        sx={{height:'40px', color:'#618264', backgroundColor: 'fff', borderColor:'#618264'}}>
          <MenuItem value={'fam_ID'}>fam_ID</MenuItem>
          <MenuItem value={'Real_name'}>Fname</MenuItem>
          <MenuItem value={'Last_name'}>Lname</MenuItem>
        </Select>
      </FormControl>
    </Box>
                        </li>
                        <li className="">
                            <Link to="/genogram" className="golink">
                                <div>
                                    <Button variant="outlined" sx={{marginLeft:'10px', marginRight: '35px', marginTop:'10px', height:'40px',
                                color: '#618264', borderColor: '#618264', '&:hover':{
                                    backgroundColor: '#B0D9B1',
                                    borderColor: '#fff',
                                }, '&:active': {
                                    borderColor: '#fff'
                                }}}>GO!</Button>
                                </div>
                            </Link>
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <div className="auto">
                    <ul>
                        <li className="auto-item">
                        <FormControlLabel control={<Checkbox defaultChecked color="success"/>} label="Auto Generate Missing Data" sx={{
                            color: '#618264', '&.Mui-checked': {backgroundColor: '#618264'},}}/>
                        </li>
                    </ul>
                </div>
            </li>
        </ul>
    </div>
  );
};

export default Search;
