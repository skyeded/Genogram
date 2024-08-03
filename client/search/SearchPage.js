import React from 'react';
import {Link} from "react-router-dom";
import ReactDOM from 'react-dom/client';

import Search from './Search';
import ShapeLogin from './shapeCompLogin';
import HomeIcon from './homeIcon';

const SearchPage = () => {
    return (
      <div>
        <HomeIcon />
        <Search />
        <ShapeLogin />
      </div>
    );
  };
  export default SearchPage;