import React from 'react';

class Element extends React.Component {
    constructor(props){
        super(props);

            this.state = {
                selected: "",
                click: {
                    x:0, y:0
                },
                up: {
                    x:0, y:0
                }
            }
    };
    getClass(id){
        var ele = this.props.data;
        var classes = [];
        classes.push('element');
        classes.push('period-' + ele.period)
        classes.push('posx-' + ele.xpos)
        classes.push('posy-' + ele.ypos)
        classes.push((id ===  this.state.selected) ? 'active' : 'default');
        return classes.join(' ');
    }
    render(){
        var ele = this.props.data;
        var width = this.props.eleWidth;
        var eleStyle = {
            left:(ele.xpos-1) * width,
            top: (ele.ypos-1) * width,
            width: width,
            height: width,
            fontSize: Math.floor(this.props.eleWidth / 10)
        };
        return(
            <div
                className={this.getClass(ele.number)}
                style={eleStyle}>
                <div className="in-element">
                    <span className="number" title="Atomic number">{ele.number}</span>
                    <span className="atomic_mass" title="Atomic mass">{ele.atomic_mass}</span>
                    <span className="symbol">{ele.symbol}</span>
                    <span className="name">{ele.name}</span>
                </div>
            </div>      
        );
    }



}




export default Element;