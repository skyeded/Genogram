import React from 'react';
import {Link} from "react-router-dom";
import ReactDOM from 'react-dom/client';

import TopNavBar from './topNavBar';
import MidSec from './midSec'
import ShapeComponent from './shapeComp';

const HomeAfterLogin = () => {
  return (
    <div class="Home">
      <div className='Top'>
        <TopNavBar />
      </div>
      <div className='Mid'>
        <MidSec />
      </div>
      <div className='Bot'>
        <ShapeComponent/>
      </div>
    </div>
  );
};
export default HomeAfterLogin;
