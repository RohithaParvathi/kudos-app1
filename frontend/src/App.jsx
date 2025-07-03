import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [users, setUsers] = useState([])
  const [kudos, setKudos] = useState([])
  const [fromUser, setFromUser] = useState("")
  const [toUser, setToUser] = useState("")
  const [message, setMessage] = useState("")

  useEffect(() => {
    axios.get("http://localhost:8000/api/users/").then(res => setUsers(res.data))
    axios.get("http://localhost:8000/api/kudos/").then(res => setKudos(res.data))
  }, [])

  const giveKudos = () => {
    axios.post("http://localhost:8000/api/kudos/", {
      from_user: fromUser,
      to_user: toUser,
      message: message
    }).then(() => {
      alert("Kudos sent!")
    })
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Kudos App</h2>

      <h3>Give Kudos</h3>
      <select onChange={e => setFromUser(e.target.value)}>
        <option>Select From User</option>
        {users.map(u => <option key={u.id} value={u.id}>{u.name}</option>)}
      </select>
      <select onChange={e => setToUser(e.target.value)}>
        <option>Select To User</option>
        {users.map(u => <option key={u.id} value={u.id}>{u.name}</option>)}
      </select>
      <input type="text" placeholder="Message" onChange={e => setMessage(e.target.value)} />
      <button onClick={giveKudos}>Send</button>

      <h3>Kudos Received</h3>
      <ul>
        {kudos.map(k => (
          <li key={k.id}>
            From {k.from_user} to {k.to_user}: {k.message}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
