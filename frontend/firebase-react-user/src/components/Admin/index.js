import React from 'react';

const Admin = () => (
    <div>
        <h1> Admin </h1>
    </div>
);

export default Admin;

/**
 * This was to test if the Firebase platform and React 
 * framework was connected
 */

// import React from 'react';
// import  { FirebaseContext } from '../Firebase';
// const SomeComponent = () => (
//   <FirebaseContext.Consumer>
//     {firebase => {
//       return <div>I've access to Firebase and render something.</div>;
//     }}
//   </FirebaseContext.Consumer>
// );
// export default SomeComponent;