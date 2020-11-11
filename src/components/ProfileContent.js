import React, { useState, useEffect } from 'react';
import './FormContent.css';
import { makeStyles } from '@material-ui/core/styles';
import { Typography } from '@material-ui/core';
import { Form, Input, Button } from 'semantic-ui-react';


const useStyles = makeStyles(theme => ({
  toolbar: theme.mixins.toolbar,
  title: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
    padding: theme.spacing(3),
    fontSize: 30,
    textAlign: "center",
  },
  content: {
    textAlign: "center",
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  fullWidth: {
    width: '100%',
  },
  labels: {
    alignContent: "center",
    textAlign: "center",
    marginLeft: 10,
    marginBottom: 10,
    display: 'block',
  },
  inputs: {
    margin: "auto",
    alignContent: "center",
    textAlign: "center",
    marginBottom: 10,
    display: 'block',
  },
  cancelbtn:{
    fontSize: 20,
    marginLeft: 300,
    marginRight: 20,

  },
  centered: {
    display: 'block',
    marginLeft: 'auto',
    marginRight: 'auto',
  },
}));




function ProfileContent() {
  const classes = useStyles();
  const [currentuser, getCurrentUser] = useState([]);

  useEffect(() => {
      fetch("/currentuser").then(response =>
          response.json().then(data => {
              getCurrentUser(data);
      })
  );
  }, []);

  const [clothes, getClothes] = useState([]);

  useEffect(() => {
      fetch("/clothing").then(response =>
          response.json().then(data => {
              getClothes(data);
      })
  );
  }, []);

  const numOfClothes = clothes.length;
  console.log(currentuser);

  return (
    <main className={classes.fullWidth}>
      <div className={classes.toolbar} />

      <img className ={classes.centered} src={process.env.PUBLIC_URL + 'ella.jpeg'}/>
      <div className={classes.content}>
        <Typography paragraph>
          Welcome, {currentuser.first_name}. Hope you're enjoying {currentuser.location}! Oops here's your password {currentuser.password}.
        </Typography>
        <Typography paragraph>
          So far, you have uploaded {numOfClothes} different clothing item(s). Make sure to update your matches
          so that we can generate your favorite outfits!
        </Typography>


      </div>
    </main>
  );
}

export default ProfileContent;
