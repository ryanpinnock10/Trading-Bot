import React from 'react';
import Positions from '../components/Portfolio/watchlist';
import axios from 'axios';

const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    title: `ant design part ${i}`,
    quantity: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    bought_price:
      'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    current_price:
      'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
  });
}

class PositionsList extends React.Component{

    state = {
        positions: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/positions/')
            .then(res => {
                this.setState({
                    positions: res.data
                });
                console.log(res.data)
            })
    }

    render() {
        return(
            <Positions data = {this.state.positions}/>
        )
    }
}

export default PositionsList