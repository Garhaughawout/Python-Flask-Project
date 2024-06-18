import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from '../components/Navbar';
import PropertyList from '../components/PropertyList';
import PropertyDetail from '../components/PropertyDetail';
import AddProperty from '../components/AddProperty';
import Register from '../components/Register';
import Login from '../components/Login';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={PropertyList} />
        <Route path="/properties" exact component={PropertyList} />
        <Route path="/properties/:id" component={PropertyDetail} />
        <Route path="/add-property" component={AddProperty} />
        <Route path="/register" component={Register} />
        <Route path="/login" component={Login} />
      </Switch>
    </Router>
  );
};

export default App;