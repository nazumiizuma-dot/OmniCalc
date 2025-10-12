import Link from 'next/link'
export default function Home(){
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#071028] via-[#0b1220] to-[#071028] p-6">
      <div className="max-w-4xl w-full">
        <header className="flex items-center justify-between mb-8 text-white">
          <h1 className="text-3xl font-bold">OmniCalc Pro</h1>
          <nav><Link href='/dashboard'>Dashboard</Link></nav>
        </header>
        <main className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <a href="/dashboard" className="p-6 rounded-2xl backdrop-blur-sm bg-white/6 border border-white/10">Dashboard</a>
          <a href="/playground" className="p-6 rounded-2xl backdrop-blur-sm bg-white/6 border border-white/10">Playground</a>
          <a href="/calculator/algebra%2Fquadratic" className="p-6 rounded-2xl backdrop-blur-sm bg-white/6 border border-white/10">Quadratic</a>
        </main>
      </div>
    </div>
  )
}
