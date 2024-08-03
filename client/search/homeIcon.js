import React from 'react';
import { Link } from 'react-router-dom';

import './homeIcon.css';

const homeIcon = () => {
  return (
    <div className="top-icon">
        <div className = "left-icon">
            <Link to="/">genogram</Link>
        </div>
    </div>
  );
};

export default homeIcon;
