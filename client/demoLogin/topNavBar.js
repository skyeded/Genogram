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
            <Link to="/search">Search</Link>
          </li>
          <li>
            <Link to="/newData">Add Data</Link>
          </li>
          <li>
            <Link to="/contact">History</Link>
          </li>
        </ul>
      </nav>
      <nav className="right-nav-bar">
        <a>Welcome <a1>Boonyakorn!</a1></a>
      </nav>
    </div>
  );
};

export default TopNavBar;