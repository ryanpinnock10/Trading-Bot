import React from 'react';
import { compose } from 'recompose';
import WatchList from './watchlist';
import OrderHistory from './OrderHistory';
//import graphQ  from '../Portfolio/stockGraph';

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


export default Landing;
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../store/actions/auth';

const { Header, Content, Footer } = Layout;

class CustomLayout extends React.Component {
    render() {
        return (
            <Layout className="layout">
                <Header>
                <div className="logo" />
                <Menu
                    theme="dark"
                    mode="horizontal"
                    defaultSelectedKeys={['2']}
                    style={{ lineHeight: '64px' }}
                >
    
                {
                    this.props.isAuthenticated ?
    
                    <Menu.Item key="2" onClick={this.props.logout}>
                        Logout
                    </Menu.Item>
    
                    :
    
                    <Menu.Item key="2">
                        <Link to="/login">Login</Link>
                    </Menu.Item>
                }
    
                    <Menu.Item key="1">
                        <Link to="/">Posts</Link>
                    </Menu.Item>
                    
                </Menu>
                </Header>
                <Content style={{ padding: '0 50px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item><Link to="/">Home</Link></Breadcrumb.Item>
                    <Breadcrumb.Item><Link to="/">List</Link></Breadcrumb.Item>
                </Breadcrumb>
                    <div style={{ background: '#fff', padding: 24, minHeight: 280 }}>
                        {this.props.children}
                    </div>
                </Content>
                <Footer style={{ textAlign: 'center' }}>
                Ant Design ©2016 Created by Ant UED
                </Footer>
            </Layout>
        );
    }
}

const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(actions.logout()) 
    }
}
