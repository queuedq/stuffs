import { withRouter } from 'next/router'
import Layout from '../components/MyLayout.js'

const Content = withRouter(({ router }) => (
  <>
    <h1>{router.query.title}</h1>
    <p>This is the blog post content.</p>
  </>
))

const Page = () => (
  <Layout>
    <Content />
  </Layout>
)

export default Page
