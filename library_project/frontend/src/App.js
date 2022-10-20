// import logo from './logo.svg';
import './App.css';

import React from 'react';
import axios from 'axios';
import {useState,useEffect} from 'react'

class App extends React.Component {
  constructor(props){

    super(props);
    this.state ={
      todoList:[],
      activeItem:{
        id:null,
        title:'',
        subtitle:'',
        author:'',
        isbn:'',
      },
    }
    this.fetchTasks= this.fetchTasks.bind(this)
  };
  componentWillMount(){
    this.fetchTasks()
  }
  fetchTasks(){
    console.log('fetching....')
    fetch('http://127.0.0.1:8000/api/')
      
    .then(response => response.json())
    .then(data => 
      this.setState({
        todoList:data})
    )
  }
    // axios.get('http://127.0.0.1:8000/api/')
     
  
 
    
  
render(){
  var tasks = this.state.todoList
  return (
      <div>
      
        <h3>Django framework</h3>
        {tasks.map(function(task,index){
          return (
            <div key = {index}>
               <h1>{task.title}</h1> 
               <span>{task.subtitle}</span>
               <p>{task.author}</p>
               <p>{task.isbn}</p>
              

            </div>
          )
        })}
          

      </div>

    )
    
}
}
export default App