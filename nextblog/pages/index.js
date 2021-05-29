import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

// export default function Home() {
//   return (
    

const Index = () => {
  const classes = useStyles();
  return (
    <React.Fragment>
      <CssBaseline />
      <Header />
      <Container maxWidth="lg" className={classes.container}>
        <Box my={4} display="flex" justifyContent="center">
          <Typography variant="h4" component="h1" gutterBottom>
            Featured Blog posts
          </Typography>
        </Box>
        <Grid container spacing={4}>
          {blogPosts.map(post => (
            <PostCard key={post.title} post={post} />
          ))}
        </Grid>
      </Container>
      <Footer title="My Blog" description="Hi there, this is my blog!" />
    </React.Fragment>
  );
};


    
//   )
// }
