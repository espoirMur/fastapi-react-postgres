// src/components/UserList.js
import React, { useState, useEffect } from "react";
import DisplayUsers from "./DisplayUsers";
import Client from "./Client";

const ListUsers = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    Client.listUsers((data) => {
      setUsers(data);
    });
  }, [users]);
  return (
    <div>
      <h1>User List</h1>
      {users.length > 0 ? (
        <DisplayUsers users={users} />
      ) : (
        <p>Loading users...</p>
      )}
    </div>
  );
};

export default ListUsers;
