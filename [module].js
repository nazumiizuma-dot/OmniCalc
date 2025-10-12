import { useRouter } from 'next/router'
import { useState } from 'react'
import axios from 'axios'
export default function CalculatorPage(){
  const router = useRouter()
  const { module } = router.query
  const [payload, setPayload] = useState('{}')
  const [result, setResult] = useState(null)
  const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"
  const submit = async () => {
    try {
      const path = `/api/v1/calculators/${module}`
      const resp = await axios.post(apiUrl + path, JSON.parse(payload))
      setResult(resp.data)
    } catch (e) {
      setResult({error: e.message})
    }
  }
  return (
    <div className="min-h-screen p-8 text-white">
      <h1 className="text-2xl mb-4">Calculator: {module}</h1>
      <textarea className="w-full p-3 mb-4 bg-white/5 rounded" value={payload} onChange={(e)=>setPayload(e.target.value)} />
      <button className="px-4 py-2 bg-purple-600 rounded" onClick={submit}>Run</button>
      <pre className="mt-4 bg-black/40 p-4 rounded">{JSON.stringify(result, null, 2)}</pre>
    </div>
  )
}
