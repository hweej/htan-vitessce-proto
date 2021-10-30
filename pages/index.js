import Head from 'next/head';
import dynamic from 'next/dynamic';



// Example view config, we need to turn this into js api
import myViewConfig from '../public/vitessce-configs/example-visium';

// Dynamic Client-side loading via nextjs dynamic
const Vitessce = dynamic(
  () => import('../components/VitessceWrapper'),
  { ssr: false }
)

export default function Home() {
  return (
    <div>
      <Head>
        <title>Vitessce Prototyping</title>
        <meta name="description" content="" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <p>Vitessce Example 1</p>
      <Vitessce
            config={myViewConfig}
            height={800}
            theme="dark"
        />
    </div>
  )
}
