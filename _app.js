import '../styles/globals.css'
import ParticlesBackground from '../components/ParticlesBackground'
export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <ParticlesBackground />
      <Component {...pageProps} />
    </>
  )
}
