/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useRef } from "react"
import { Box, Button, Center, Flex, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import { ColorModeContext, EventLoopContext } from "/utils/context"
import { Event, refs } from "/utils/state"
import { MoonIcon } from "@chakra-ui/icons"
import Script from "next/script"
import NextHead from "next/head"



export function Button_a221cde1011ecfcf50b1c6934cc175da () {
  const [addEvents, connectError] = useContext(EventLoopContext);
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)

  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, colorMode, toggleColorMode])

  return (
    <Button onClick={on_click_9922dd3e837b9e087c86a2522c2c93f8} sx={{"color": "#133e7c"}}>
  <MoonIcon/>
</Button>
  )
}

export default function Component() {
  const ref_countdown = useRef(null); refs['ref_countdown'] = ref_countdown;

  return (
    <Fragment>
  <Box>
  <VStack sx={{"bg": "#711c91", "position": "sticky", "borderBottom": "0.50em solid #0abdc6", "paddingX": "1em", "paddingY": "1em", "zIndex": "700", "top": "0"}}>
  <HStack sx={{"width": "100%", "fontSize": "1.5em"}}>
  <ChakraImage alt={`logo de wicked nails`} src={`wickednails.png`} sx={{"width": "3em", "height": "3em"}}/>
  <Text>
  {`Wicked Nails`}
</Text>
  <Spacer/>
  <Link as={NextLink} className={`nes-icon instagram is-medium`} href={`https://www.instagram.com/wicked_nails_studio/`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#091833", "textDecoration": "none"}}}>
  {``}
</Link>
</HStack>
</VStack>
  <Center>
  <VStack spacing={`3em`} sx={{"width": "100%"}}>
  <VStack sx={{"alignItems": "start", "paddingX": "1.5em", "width": "100%", "maxWidth": "1000PX", "paddingTop": "3em"}}>
  <Button_a221cde1011ecfcf50b1c6934cc175da/>
  <Heading size={`lg`} sx={{"font": "Orbitron", "paddingBottom": "1em", "fontSize": "3em", "fontFamily": "Orbitron", "color": "#0abdc6"}}>
  {`Wicked Nails 2024`}
</Heading>
  <Flex sx={{"flexDirection": ["column", "column", "column", "row", "row"]}}>
  <ChakraImage alt={`imagen logo`} src={`wickednails.png`} sx={{"width": "16em", "height": "16em", "marginRight": "1.5em"}}/>
  <VStack>
  <Box className={`nes-container is-dark`} sx={{"fontSize": "1.5em"}}>
  <Text>
  {`Feliz Dia`}
</Text>
  <Text>
  {`Para Todos`}
</Text>
</Box>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  {`Pagina de Nails `}
  <Text as={`span`} sx={{"color": "#091833", "fontSize": "1em"}}>
  {`Se Feliz `}
</Text>
  {`;-)`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  {`Como Estas?`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  {`Sera Genial!!`}
</Text>
  <Link as={NextLink} href={`https://www.instagram.com/explore/tags/nailaddict/`} isExternal={true} sx={{"color": "#133e7c", "paddingTop": "1.5em", "fontSize": "0.8em", "textDecoration": "none", "_hover": {"color": "#091833", "textDecoration": "none"}}}>
  {`#nailsaddict`}
</Link>
</VStack>
</Flex>
</VStack>
  <VStack>
  <HStack spacing={`1em`} sx={{"paddingBottom": "2.25"}}>
  <Box className={`nes-icon is-medium `}/>
  <Heading size={`md`} sx={{"color": "#091833", "fontFamily": "Orbitron"}}>
  {`Wicked Nails`}
</Heading>
</HStack>
  <VStack>
  <HStack alignItems={`start`}>
  <Text>
  {`hoy es: `}
</Text>
  <Text id={`countdown`} ref={ref_countdown}/>
</HStack>
</VStack>
  <Script src={`/dev/assets/js/date.js`} strategy={`afterInteractive`}/>
</VStack>
  <HStack sx={{"alignItems": "start", "paddingX": "1.5em", "width": "100%", "maxWidth": "1000PX"}}>
  <Flex sx={{"alignItems": "center", "width": "100%", "fontSize": "0.5em"}}>
  <ChakraImage alt={`Clienta unas`} src={`nails1.png`} sx={{"width": "16em", "height": "16em"}}/>
  <ChakraImage alt={`Clienta unas`} src={`nails2.png`} sx={{"width": "16em", "height": "16em"}}/>
  <ChakraImage alt={`Clienta unas`} src={`nails1.png`} sx={{"width": "16em", "height": "16em"}}/>
  <ChakraImage alt={`Clienta unas`} src={`nails2.png`} sx={{"width": "16em", "height": "16em"}}/>
  <ChakraImage alt={`Clienta unas`} src={`nails2.png`} sx={{"width": "16em", "height": "16em"}}/>
  <ChakraImage alt={`Clienta unas`} src={`nails1.png`} sx={{"width": "16em", "height": "16em"}}/>
  <ChakraImage alt={`Clienta unas`} src={`nails2.png`} sx={{"width": "16em", "height": "16em"}}/>
</Flex>
</HStack>
  <Box sx={{"alignItems": "start", "paddingX": "1.5em", "width": "100%", "maxWidth": "1000PX"}}>
  <VStack alignItems={`center`} className={`nes-container is-dark with-title is-centered`} sx={{"width": "100%", "fontSize": "0.5em"}}>
  <Text className={`title`} sx={{"color": "#091833", "fontSize": "0.8em"}}>
  {`¿Cómo agendar una cita?`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  <Box className={`nes-icon trophy is-small`}/>
  {` Escribeme al Whatsapp.`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  <Box className={`nes-icon trophy is-small`}/>
  {` Indicame el dia y la hora.`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  <Box className={`nes-icon trophy is-small`}/>
  {` Enviame Tu Diseño, Por Favor!`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  <Box className={`nes-icon trophy is-small`}/>
  {` Confirmare Tu Cita, Nos Vemos Pronto.`}
</Text>
  <Text as={`span`} sx={{"fontSize": "1.5em"}}>
  <Box className={`nes-icon trophy is-small`}/>
  {` Recuerda Siempre dejar tu Reseñas en mis redes, estare muy Agradecida.`}
</Text>
  <Link as={NextLink} href={`https://www.instagram.com/wicked_nails_studio/`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#091833", "textDecoration": "none"}}}>
  <Button className={`nes-btn is-primary`}>
  {`Instagram`}
</Button>
</Link>
</VStack>
</Box>
  <HStack sx={{"alignItems": "start", "paddingX": "1.5em", "width": "100%", "maxWidth": "1000PX", "paddingBotton": "1.5em"}}>
  <VStack alignItems={`center`} spacing={`0.8em`}>
  <Text sx={{"fontSize": "0.8em", "marginBottom": "0.5em"}}>
  {`Lorena Garrido Campos. Manicurista Profesional`}
</Text>
  <Link as={NextLink} href={`https://www.instagram.com/wicked_nails_studio/`} isExternal={true} sx={{"fontSize": "0.8em", "color": "#ea00d9", "textDecoration": "none", "_hover": {"color": "#091833", "textDecoration": "none"}}}>
  {`Creada Con  `}
  <Box className={`nes-icon is-small heart`}/>
  {`  para Mis Clientas.`}
</Link>
</VStack>
  <Spacer/>
  <ChakraImage alt={`logo wickednails`} className={`nes-avatar is-large`} src={`wickednails.png`}/>
</HStack>
</VStack>
</Center>
</Box>
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
