/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Box } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Box/>
  <NextHead>
  <title>
  {`Wicked Nails`}
</title>
  <meta content={`Un Encanto en Tus Unas`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
