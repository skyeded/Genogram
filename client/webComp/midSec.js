import React from 'react';
import { Link } from 'react-router-dom';
import Checkbox from '@mui/material/Checkbox';

import './midSec.css'; // Import the CSS file
import homeImage from './images/homeImage.png'

const MidSec = () => {
  return (
    <div className = "MidElements">
        <div className = "midTexts">
            <ul>
                <li>
                    View & Edit your family tree here.
                </li>
                <li>
                    Our website offers multiple features relating to
                    <br />
                    your family tree using genogram!
                </li>
                <li>
                    <Link to="/search">Lets Begin!</Link>
                </li>
            </ul>
        </div>
        <div className = "imageAlign">
            <img src = {homeImage} alt="image" />
        </div>
    </div>
  );
};

export default MidSec;