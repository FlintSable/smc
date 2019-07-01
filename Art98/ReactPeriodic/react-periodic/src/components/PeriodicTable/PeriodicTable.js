import React, { Component } from 'react';
import Element from '../Elements/Element.js';
import withSizes from 'react-sizes'


class PeriodicTable extends React.Component {

    constructor(props) {
        super(props);
        
        this.state = {
            data: require('../../data/PeriodicTableJSON.json'),
            elWidth: Math.floor((props.winWidth) / 18),
            hold: false,
            catchX: null,
            catchY: null,
            periodicLeft: null,
            periodicTop: null,
            left: 0,
            top: 0,
            scale: this.props.scale,
            current: null,
        }
    }
    componentDidMount() {
        var h = this.props.winHeight - this.periodicX.offsetTop;
        this.periodicX.style.height = h + 'px';
        var initialTop = (h - this.state.elWidth * 10) / 2;
        //console.log(this.state, this.state.elWidth*2, this.props.winHeight*2, initialTop);
        this.setState({
            top: initialTop
        });
    }
    catch(event) {
        //console.log(event.touches[0].pageX);
        //var periodic = this.periodicElement;
        var co = this.getPageCoordinates(event);
        this.setState(
            {
                hold: true,
                catchX: co.x,
                catchY: co.y,
                periodicLeft: this.state.left,
                periodicTop: this.state.top,
            }
        );
        //console.log(this.state);
    }
    // on MouseMove
    move(event) {
        if (!this.state.hold) {
            return false;
        }
        //var periodic = this.periodicElement;
        var co = this.getPageCoordinates(event);

        var offsetX = this.state.catchX - co.x;
        var offsetY = this.state.catchY - co.y;
        //console.log(event.pageY, this.state.catchY);

        //var m = periodic.style['margin-left'].replace('px', '');
        //console.log(this.state.leftX);
        this.setState({
            left: this.state.periodicLeft - offsetX,
            top: this.state.periodicTop - offsetY
        });
    }
    // onMouseUp
    leave(event) {
        //var periodic = this.periodicElement;
        this.setState(
            {
                hold: false,
            }
        );
    }
    getClass() {
        var classes = ['periodic'];
        if (this.state.hold) {
            classes.push('hold');
        }
        return classes.join(' ');
    }
    // returns pageX and pageY for mobile and desktop
    getPageCoordinates(event)
    {
        return {
            x: event.pageX ? event.pageX : event.touches[0].pageX,
            y: event.pageY ? event.pageY : event.touches[0].pageY,
        }
    }
    render() {
        this.setState(this.props.scale);

        var myStyle = {
            height: 10*this.state.elWidth,
            marginTop: this.state.top,
            marginLeft: this.state.left,
            transform: 'scale(' + this.state.scale +')', 
        };

        var showItem = (this.state.current !== null ? true : false);
        //console.log(this.state.current, showItem)
        var currentData = this.state.current !== null ? this.state.data.elements[this.state.current] : null;
        //console.log(currentData);
        return (
            <div className="periodic-x">
                <div className="periodic-c"
                    ref={(ref) => { this.periodicX = ref; }}>
                    <div 
                        className = {this.getClass()} 
                        style = {myStyle} 
                        ref = {(ref) => { this.periodicElement = ref; }} >

                        {this.state.data.elements.map((element, i) => <Element 
                            key = {i}
                            index = {i}
                            data = {element} 
                            elWidth = {this.state.elWidth}
                         
                         />)}
                         
                    </div>
                </div>
            </div>
        );
    }
 }

const mapSizesToProps = ({ width, height }) => ({
    winWidth: width,
    winHeight: height,
})

export default withSizes(mapSizesToProps)(PeriodicTable)