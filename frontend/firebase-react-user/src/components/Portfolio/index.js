import React from 'react';
import { compose } from 'recompose';

import { withAuthorization, withEmailVerification } from '../Session';
//import Messages from '../Messages';
import wList from './watchlist';
const HomePage = () => (
  <div>
    {/* <h1>Portfolio</h1>
    <p>The Portfolio Page is accessible by every signed in user.</p>

    <Messages /> */}
      {wList}
  </div>
);

const condition = authUser => !!authUser;

export default compose(
  withEmailVerification,
  withAuthorization(condition),
)(HomePage);
