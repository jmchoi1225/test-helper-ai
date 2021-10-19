import React from 'react'
import Todolist from './Todolist'

function TestStudentMobileSetting(){
  return(
    <div className="m-5 p-5"> 
      <Todo></Todo>
    </div>
  )
}
function Todo(){
  let pagetitle="TestStudentMobileSetting"
  let todos=["모바일로 페이지에 접속한다.","모바일로 화상회의에 접속한다.","모바일 화면 공유 및 모바일 마이크 공유가 화상회의를 통해 master channel으로 스트리밍 잘 되는지 확인한다.","모바일 공유화면 녹화본이 AWS S3에 업로드 되는지 확인한다."]
  let names=["승현","지연","지연","승현"]
  let dates=["","","",""]
  let status=["To do","To do","To do","To do"]
  return(
    <Todolist pagetitle={pagetitle} todos={todos} names={names} dates={dates} status={status} ></Todolist>
  )
}
export default TestStudentMobileSetting