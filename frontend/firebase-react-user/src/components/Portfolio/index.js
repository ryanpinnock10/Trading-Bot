import React from 'react';
import { compose } from 'recompose';
// import WatchList from '../Portfolio/watchlist';
// import OrderHistory from '../Portfolio/OrderHistory';

import { withAuthorization, withEmailVerification } from '../Session';
import Messages from '../Messages';

const HomePage = () => (
  <div>
    <h1>Portfolio</h1>
    <p>The Portfolio Page is accessible by every signed in user.</p>

    <Messages />
    {/* <WatchList/>
    <OrderHistory/> */}
  </div>
);

const condition = authUser => !!authUser;

export default compose(
  withEmailVerification,
  withAuthorization(condition),
)(HomePage);
