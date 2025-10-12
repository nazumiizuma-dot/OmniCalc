import { useState } from 'react'
import axios from 'axios'
export default function Playground(){
  const [expr, setExpr] = useState('')
  const [res, setRes] = useState(null)
  const callAi = async () => {
    const resp = await axios.post((process.env.NEXT_PUBLIC_API_URL||'http://localhost:8000') + '/api/v1/calculators/ai/help', {expr})
    setRes(resp.data)
  }
  return (
    <div className="min-h-screen p-8 text-white">
      <h1 className="text-2xl mb-4">Playground (AI helper)</h1>
      <textarea className="w-full p-3 mb-4 bg-white/5 rounded" value={expr} onChange={(e)=>setExpr(e.target.value)} />
      <button className="px-4 py-2 bg-pink-500 rounded" onClick={callAi}>Ask AI</button>
      <pre className="mt-4 bg-black/40 p-4 rounded">{JSON.stringify(res, null, 2)}</pre>
    </div>
  )
}
