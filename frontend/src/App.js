import React, { useEffect, useState } from "react";

function App() {
  const [patients, setPatients] = useState([]);
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  useEffect(() => {
    fetch("http://flask-backend:5000/patients")
      .then(res => res.json())
      .then(data => setPatients(data));
  }, []);

  const addPatient = () => {
    fetch("http://flask-backend:5000/patients", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({name, age})
    }).then(() => window.location.reload());
  };

  return (
    <div style={{padding: "20px"}}>
      <h1>Patient List</h1>
      <input placeholder="Name" onChange={e => setName(e.target.value)} />
      <input placeholder="Age" onChange={e => setAge(e.target.value)} />
      <button onClick={addPatient}>Add</button>
      <ul>
        {patients.map((p, i) => (
          <li key={i}>{p[1]} (Age: {p[2]})</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
