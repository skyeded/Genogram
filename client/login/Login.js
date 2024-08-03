import React from 'react';
import { Link } from 'react-router-dom';

import './Login.css';

const Login = () => {
  return (
    <div className="loginBody">
        <ul>
            <li className="outer">
                Sign in
            </li>
            <li className="outer">
                Sign in and start using our web application now!
            </li>
            <li className="outer">
                Username
            </li>
            <li className="outer">
                Password
            </li>
            <li>
                <div className="forgot">
                    <ul>
                        <li className="forgot-item">
                            <div className="check">
                                <input type="checkbox" />
                                <span className="checkmark"></span>
                            </div>
                        </li>
                        <li className="forgot-item">
                            Remember me 
                        </li>
                        <li className="forgot-item">
                            Forgot password?
                        </li>
                    </ul>
                </div>
            </li>
            <li className="outer">
                <Link to="/homeAfterLogin" className="login">
                    <div>
                        Log in
                    </div>
                </Link>
            </li>
        </ul>
    </div>
  );
};

export default Login;
