// TopNavBar.js
import React from 'react';
import { Link } from 'react-router-dom';

import './topNavBar.css'; // Import the CSS file

const TopNavBar = () => {
  return (
    <div className="top-nav-container">
      <div className = "left-nav-bar">
        <div className="logoName">
          genogram
        </div>
      </div>
      <nav className="top-nav-bar">
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/newData">Add Data</Link>
          </li>
          <li>
            <Link to="/history">History</Link>
          </li>
        </ul>
      </nav>
      <nav className="right-nav-bar">
        <Link to="/loginPage" className="login-button">
          <div><a>Log in</a></div>
        </Link>
      </nav>
    </div>
  );
};

export default TopNavBar;