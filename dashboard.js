import Link from 'next/link'
const MODULES = [
  {key: "algebra/quadratic", name: "Quadratic Solver"},
  {key: "calculus/derivative", name: "Derivative"},
  {key: "calculus/integrate_numeric", name: "Integral (numeric)"},
  {key: "matrix/inverse", name: "Matrix Inverse"},
  {key: "statistics/describe", name: "Statistics"},
  {key: "physics/kinematics", name: "Kinematics"},
  {key: "converter/unit", name: "Unit Converter"},
  {key: "transform/dft", name: "DFT"},
  {key: "finance/loan", name: "Loan Calc"},
  {key: "ai/help", name: "AI Helper"},
];
export default function Dashboard(){
  return (
    <div className="min-h-screen p-8 bg-gradient-to-br from-[#0b1220] via-[#1b1f3b] to-[#071028] text-white">
      <h2 className="text-3xl mb-6">Dashboard</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {MODULES.map(m => (
          <Link key={m.key} href={`/calculator/${encodeURIComponent(m.key)}`}>
            <a className="p-4 rounded-xl bg-white/5 border border-white/10">{m.name}</a>
          </Link>
        ))}
      </div>
    </div>
  )
}
