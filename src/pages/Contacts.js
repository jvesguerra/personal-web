import React, { useEffect, useState } from 'react';

const Contacts = () => {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/people/')
      .then((response) => response.json())
      .then((data) => setPeople(data));
  }, []);

  return (
    <div className="container">
      <h1>People List</h1>
      <ul>
        {people.map((person) => (
          <h3 key={person.id}>
            {person.firstname} {person.lastname}
          </h3>
        ))}
      </ul>
    </div>
  );
};

export default Contacts;