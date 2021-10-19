import React, { useState } from 'react';
import { Nav } from 'react-bootstrap';
import {Link } from 'react-router-dom';
import TestStudentAgreement from './TestStudentAgreement'
import TestStudentPCSetting from './TestStudentPCSetting'
import TestStudentMobileSetting from './TestStudentMobileSetting'
import TestStudentIdentification from './TestStudentIdentification'
import TestStudentWaiting from './TestStudentWaiting'

function TeststudentPre(){
  let [tab,setTab]=useState(0)
  let [tabCompleted,setTabCompleted]=useState([false,false,false,false,false])
  let tabtitles=["안내사항 & 사전동의","PC화면공유","모바일화면공유 & 모바일마이크공유","본인인증"," 시험대기 "]
  let tablink=["/tests/students/agreement","/tests/students/pcsetting","/tests/students/mobilesetting","/tests/students/identification","/tests/students/waiting"]
  return(
    <div> 
      <h4 className="mb-5">이 페이지(대학생 시험준비)에선 위의 Navbar는 없을 예정.</h4>
      <hr></hr>
      <Nav variant="tabs" defaultActiveKey="link-0">
        {
          tabtitles.map((tabtitle,index)=>{
            return(
              <Nav.Item key={index}>
                <Nav.Link  as={Link} to ={tablink[index]} eventKey={"link-"+index} onClick={()=>{ setTab(index) }} >{tabtitle +" : "+ tabCompleted[index]}</Nav.Link>
              </Nav.Item>
            )
          })
        }
      </Nav>
      <Tabcontent tab={tab} tabtitles={tabtitles} tabCompleted={tabCompleted} setTabCompleted={setTabCompleted} ></Tabcontent>
    </div>
  )
}
function Tabcontent(props){
  if (props.tab===0){
    return(
      <div>
        <TestStudentAgreement tabCompleted={props.tabCompleted} setTabCompleted={props.setTabCompleted}></TestStudentAgreement>
      </div>
    )
  }
  else if (props.tab===1){
    return(
      <div>
        <TestStudentPCSetting></TestStudentPCSetting>
      </div>
    )
  }
  else if (props.tab===2){
    return(
      <div>
        <TestStudentMobileSetting></TestStudentMobileSetting>
      </div>
    )
  }
  else if (props.tab===3){
    return(
      <div>
        <TestStudentIdentification></TestStudentIdentification>
      </div>
    )
  }
  else if (props.tab===4){
    return(
      <div>
        <TestStudentWaiting tabCompleted={props.tabCompleted} tabtitles={props.tabtitles}></TestStudentWaiting>
      </div>
    )
  }
  
}
export default TeststudentPre