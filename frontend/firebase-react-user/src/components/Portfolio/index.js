import React from 'react';
import { compose } from 'recompose';
//import OrderHistory from './orderHistory/index';

import { withAuthorization, withEmailVerification } from '../Session';
import Messages from '../Messages';

import Dropdown from 'react-bootstrap/Dropdown'

const HomePage = () => (
  <div>
    <h1>Portfolio</h1>
    <p>The Portfolio Page is accessible by every signed in user.</p>

    <Messages />
    <Dropdown>
  <Dropdown.Toggle variant="success" id="dropdown-basic">
    Example Dropdown Button
  </Dropdown.Toggle>

  <Dropdown.Menu>
    <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
    <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
    <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
  </Dropdown.Menu>
</Dropdown>
  </div>
);

const condition = authUser => !!authUser;

export default compose(
  withEmailVerification,
  withAuthorization(condition),
)(HomePage);
