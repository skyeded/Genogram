import React, { useState } from 'react';
import { InputBase, Paper, IconButton } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

const SearchBar = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = () => {
    // Implement your search logic here
    console.log('Searching for:', searchTerm);
  };

  return (
    <Paper component="form" sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 400, marginBottom: '20px'}}>
      <InputBase
        placeholder="Insert your family ID..."
        inputProps={{ 'aria-label': 'search' }}
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        sx={{ marginLeft: 1, flex: 1 }} // Adjust the margin and flex properties
      />
      <IconButton type="button" onClick={handleSearch} aria-label="search">
        <SearchIcon />
      </IconButton>
    </Paper>
  );
};

export default SearchBar;
