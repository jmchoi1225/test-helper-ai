import React from 'react'
import {Table} from 'react-bootstrap'


function Todolist(props){
  return(
    <div>
      <h4>{props.pagetitle}페이지입니다.</h4>
      <br></br>
      <h5>다음과 같은 순서로 구현할 예정입니다. </h5>
      <Table className="mt-3" striped bordered hover size="sm">
        <thead>
          <tr>
            <th>#</th>
            <th>기능</th>
            <th>name</th>
            <th>예상완료날짜</th>
            <th>진행상황</th>
          </tr>
        </thead>
        <tbody>
          {
            props.todos.map((todo,index)=>{
              return(
                <tr>
                  <td>{index+1}</td>
                  <td>{todo}</td>
                  <td>{props.names[index]}</td>
                  <td>{props.dates[index]}</td>
                  <td>{props.status[index]}</td>
                </tr>
              )
            })
          }
        </tbody>
      </Table>
    </div>
  )
}
export default Todolist