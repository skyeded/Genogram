import React from 'react';
import Login from './Login';
import ShapeLogin from '../webComp/shapeCompLogin';
import HomeIcon from '../search/homeIcon';

const LoginPage = () => {
    return (
      <div>
        <HomeIcon />
        <Login />
        <ShapeLogin />
      </div>
    );
  };
  export default LoginPage;