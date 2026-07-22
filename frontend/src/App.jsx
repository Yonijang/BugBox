import { useEffect, useState } from 'react'

function App() {
  const [backendMessage, setBackendMessage] = useState('Chacking backend...')

  useEffect(() => {
    fetch('http://127.0.0.1:8000/')
    .then((Response) => Response.json())
    .then((data) => {
      setBackendMessage(data.message)
    })
    .catch (() => {
      setBackendMessage('Backend connection failed')
    })
  }, [])
  return (
    <main>
      <h1>BugBox</h1>
      <p>Personal Debugging Memory System</p>

      <h2>Backend Status</h2>
      <p>{backendMessage}</p>
    </main>
  )
}

export default App