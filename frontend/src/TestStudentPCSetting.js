import React from 'react'
import Todolist from './Todolist'

function TestStudentPCSetting(){
  return(
    <div className="m-5 p-5"> 
      <Todo></Todo>
    </div>
    
  )
}
function Todo(){
  let pagetitle="TestStudentPCSetting"
  let todos=["PC화면 공유 버튼을 누른다.","PC로 화상회의에 접속한다.","PC 공유화면이 화상회의를 통해 master channel으로 스트리밍 잘 되는지 확인한다.","PC 공유화면 녹화본이 AWS S3에 업로드 되는지 확인한다."]
  let names=["지연","지연","지연","승현"]
  let dates=["","","",""]
  let status=["To do","To do","To do","To do"]
  return(
    <Todolist pagetitle={pagetitle} todos={todos} names={names} dates={dates} status={status} ></Todolist>
  )
}
export default TestStudentPCSetting