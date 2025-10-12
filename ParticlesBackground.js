import Particles from 'react-particles-js'
export default function ParticlesBackground(){
  return (
    <div style={{position:'fixed', inset:0, zIndex:-1}}>
      <Particles params={{
        particles: {
          number: { value: 60 },
          size: { value: 3 },
          color: { value: ["#6B21A8","#F472B6","#FFFFFF"] },
          line_linked: { enable: true, color: "#ffffff", opacity: 0.04 }
        }
      }} />
    </div>
  )
}
