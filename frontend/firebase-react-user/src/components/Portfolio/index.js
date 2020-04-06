import React from 'react';
import { compose } from 'recompose';
//import OrderHistory from './orderHistory/index';

import { withAuthorization, withEmailVerification } from '../Session';
import Messages from '../Messages';

const HomePage = () => (
  <div>
    <h1>Portfolio</h1>
    <p>The Portfolio Page is accessible by every signed in user.</p>

    <Messages />
  </div>
);

const condition = authUser => !!authUser;

export default compose(
  withEmailVerification,
  withAuthorization(condition),
)(HomePage);


// import React from "react";
// //import "./styles.css";

// export default function App() {
//   return (
//     <div className="App">
//       <h1>TradeBot</h1>
//       <h2>Here is a veiw of your portfolio</h2>
//       <ul class="list">
//     <li>
//         <span class="Firstname">Jonny</span>
//         <span class="Lastname">Sundsvall</span>
//     </li>
// </ul>


//    </div>

//   );
//   }