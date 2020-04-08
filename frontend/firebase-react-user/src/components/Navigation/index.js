import React from 'react';
import {Link} from 'react-router-dom';

import { AuthUserContext } from '../Session';
import SignOutButton from '../SignOut';
import * as ROUTES from '../../constants/routes';
import * as ROLES from '../../constants/roles';
import Dropdown from 'react-bootstrap/Dropdown'

const Navigation = () => (
  <AuthUserContext.Consumer>
    {authUser =>
      authUser ? (
        <NavigationAuth authUser={authUser} />
      ) : (
        <NavigationNonAuth />
      )
    }
  </AuthUserContext.Consumer>
);

const NavigationAuth = ({ authUser }) => (

<Dropdown>
   <Dropdown.Toggle variant="success" id="dropdown-basic">
     Dropdown Button
   </Dropdown.Toggle>

   <Dropdown.Menu>
     <Dropdown.Item as={Link} eventKey={"1"} to={ROUTES.LANDING} className={''}> Landing </Dropdown.Item>
     <Dropdown.Item as={Link} eventKey={"2"} to={ROUTES.HOME}>Portfolio</Dropdown.Item>
     <Dropdown.Item as={Link} eventKey={"3"} to={ROUTES.ACCOUNT}>Account</Dropdown.Item>
     {!!authUser.roles[ROLES.ADMIN] &&(
     <Dropdown.Item> as={Link} eventKey={"4"} to={ROUTES.ADMIN}>Admin </Dropdown.Item> )}
     <Dropdown.Item> <SignOutButton /> </Dropdown.Item>
   </Dropdown.Menu>
</Dropdown>
  

/* <Dropdown.Item as={Link} eventKey={"2"} to={browseUrl} className={'Header-headerMenuLinks'}>
   <h3>Message</h3>
</Dropdown.Item> */
  
//   <ul>
//     <li>
//       <Link to={ROUTES.LANDING}>Landing</Link>
//     </li>
//     <li>
//       <Link to={ROUTES.HOME}>Portfolio</Link>
//     </li>
//     <li>
//       <Link to={ROUTES.ACCOUNT}>Account</Link>
//     </li>
//     {!!authUser.roles[ROLES.ADMIN] && (
//       <li>
//         <Link to={ROUTES.ADMIN}>Admin</Link>
//       </li>
//     )}
//     <li>
//       <SignOutButton />
//     </li>
//   </ul>
 );

const NavigationNonAuth = () => (
    <ul>
      <li>
        <Link to={ROUTES.LANDING}>Landing</Link>
      </li>
      <li>
        <Link to={ROUTES.SIGN_IN}>Sign In</Link>
      </li>
    </ul>
  );

export default Navigation;