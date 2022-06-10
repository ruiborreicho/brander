import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Brander from '../components/brander'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Brander | AI Generated Marketing</title>
        <meta name="description" content="Generate branding snippets and keywords for your product" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Brander/>
    </div>
  )
}

export default Home
