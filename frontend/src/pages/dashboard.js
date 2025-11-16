import { useEffect, useState } from 'react'
import { Line } from 'react-chartjs-2'
export default function Dashboard(){
  const [history,setHistory] = useState([])
  useEffect(()=>{
    // contoh data dummy — ganti dengan fetch real dari backend
    setHistory([0.7,0.5,0.6,0.4,0.8])
  },[])
  const data = {
    labels: history.map((_,i)=>`Day ${i+1}`),
    datasets: [{label:'Productivity score', data: history}]
  }
  return (
    <div className="p-6">
      <h2 className="text-xl mb-4">Dashboard</h2>
      <div style={{width:600}}>
        <Line data={data} />
      </div>
    </div>
  )
}
