// ShapeComponent.js
import React from 'react';
import './shapeComp.css'; // Import the CSS file

const ShapeComponent = () => {
  return (
    <div className="svgContainer">
      <svg width="1920" height="570" viewBox="0 0 1920 514" fill="none" xmlns="http://www.w3.org/2000/svg" className="homeShape">
        <path d="M335.113 85.5293C88.9931 -171.561 -81.5123 211.766 -136 435.566V560H2208V435.566C1686.25 426.008 581.233 342.62 335.113 85.5293Z" fill="#D0E7D2"/>
      </svg>
    </div>
  );
};

export default ShapeComponent;