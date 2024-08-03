import {Link} from "react-router-dom";
import ReactDOM from 'react-dom/client';
import './historyPage.css';
import App from '../App';
import HomeIcon from 'C:/Users/User/Desktop/CS400/client/src/search/homeIcon.js'
import TextField from '@mui/material/TextField';
import React, { useState } from 'react';

import HistoryTable from './HistoryTable';
import SearchBar from "../webComp/searchBar";

const HistoryPage = () => {
    return (
        <div>
            <div className='homeicon'>
                <HomeIcon></HomeIcon>
            </div>
            <div className='searchHistory'>
                <SearchBar/>  
            </div>
            <div className='historylabel'>
                <a>History</a>
            </div>
            <div className='historytable'>
                <HistoryTable></HistoryTable>
            </div>
        </div>
    );
  };
  export default HistoryPage;