import React from 'react'
import {ListGroup} from 'react-bootstrap'
import Todolist from './Todolist'

function TestStudentWaiting(props){
  console.log(props.tabCompleted)
  return(
    <div className="m-5 p-5"> 
      <Todo></Todo>
      <ListGroup>
        {props.tabCompleted.map((completed,index)=>{
          return (
            <ListGroup.Item key={index} action variant="info">
              {props.tabtitles[index] +" 성공여부 "+props.tabCompleted[index]}
            </ListGroup.Item>
          )
        })}
      </ListGroup>
    </div>
  )
}
function Todo(){
  let pagetitle="TestStudentWaiting"
  let todos=["안내사항 & 사전동의가 완료되었는지 보여준다.","PC화면 공유가 완료되었는지 보여준다.","모바일 화면 공유 및 모바일 마이크 공유가 완료되었는지 보여준다.","본인인증이 완료되었는지 보여준다.","시험 시작시간까지 남은 시간을 보여준다.","시험 시작시간이 되면 시험장 입장 버튼을 활성화한다","시험장 입장(시험문제페이지)로 접속할수 있도록한다."]
  let names=["승현","승현","승현","승현","승현","승현","승현"]
  let dates=["10.19 화","10.19 화","10.20 수","10.21 목","10.19 화","10.19 화","10.19 화"]
  let status=["In progress","In progress","To do","To do","To do","In progress","In progress"]
  return(
    <Todolist pagetitle={pagetitle} todos={todos} names={names} dates={dates} status={status} ></Todolist>
  )

}
export default TestStudentWaiting