#include "colors.inc"                       
#include "stones.inc" 
#include "textures.inc"  
#include "shapes.inc"
#include "glass.inc"
#include "metals.inc"
#include "woods.inc"

camera {
    location <-7, 6.9, -6>
    look_at  <1.4, .2,  2.5>
    angle 25
}
background { color rgbt<1,1,1, 0> }  


#declare gold = material{
texture {
pigment { color Gold }
finish {
ambient 0.2
diffuse 0.2
reflection 0.8
//specular 1
roughness .001
}
}
}


global_settings {
max_trace_level 10
photons {
count 100000
autostop 0
media 100
max_trace_level 10
}
}
light_source { <-500,500,-500> 1.5*White
media_interaction off
media_attenuation off
photons { reflection off refraction off }
}


 // // // // //// SUBSTRATE SILICON // // // // // // // // // // // // // // //
object {
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1.7, 0.4, 1.>,<2.3, -0.1,-1.9 >, 0.125, 0)
     texture{ //pigment{color SteelBlue}
       Chrome_Metal
//     Brass_Metal
    }   
     rotate <0,10,0>
     translate 0.6*y
     translate 2.0*z
} //  
     
 
  // // // // //// // // // //  BOTTOM ELECTRODE  // // // // //// // // // // //// // // // // //// // // // // ////
     
object {                   ///          
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1.25, 0.5, -1.2>,<-0.8, 0.4,0.7 >, 0.05, 0)   
//  Round_Box(<-1.5, 0, -1>,< 1.8, 0.2,1.3>, 0.125, 0)
texture{Copper_Metal}  rotate <0,10,0>    translate 0.6*y      translate 2.0*z
} //

object {                   ///          
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1., 0.5, -0.95>,<-1.05, 0.4,-1.55 >, 0.05, 0)  
texture{Copper_Metal}  rotate <0,10,0>    translate 0.6*y      translate 2.0*z
} //

object {                   ///          
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1.25, 0.5, -1.35>,<-0.8, 0.4,-1.75 >, 0.05, 0)  
texture{Copper_Metal}  rotate <0,10,0>    translate 0.6*y      translate 2.0*z
} //


object {                /// GATE ELECTRODE CONTACT 
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.56, 0.5, -1.2>,<-0.15, 0.4,0.55 >, 0.05, 0) 
//  Round_Box(<2.5, 0.5, -0.9>,<1.15, 0.49,-1.2 >, 0.05, 0)
     texture{
     Copper_Metal
    }   
     rotate <0,10,0>
     translate 0.6*y
     translate 2.0*z
} //           

object {                   ///          
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<0.63, 0.5, -.95>,<0.68, 0.4,-1.55 >, 0.05, 0)  
texture{Copper_Metal}  rotate <0,10,0>    translate 0.6*y      translate 2.0*z
} //

object {                   ///          
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<0.44, 0.5, -1.35>,<.9, 0.4,-1.75 >, 0.05, 0)  
texture{Copper_Metal}  rotate <0,10,0>    translate 0.6*y      translate 2.0*z
} //



//////////////////   DIELECTRIC  //////////////////////////////////////////

object {                             //// DIELECTRIC 111      BIG BIG BIG 
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-0.83, 0.6, -1.15>,<2.05, 0.3,0.68 >, 0.01, 0.) 
     texture{
pigment{ color rgbt<1,0.7,0, 0.2>}
    }   
     rotate <0,10,0>
     translate 0.6*y
     translate 2.0*z
} //
     

object {                             //// DIELECTRIC 222
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1.35, 0.6, 0.0>,<-.83, 0.3,0.68 >, 0.01, 0.) 
     texture{
pigment{ color rgbt<1,0.7,0, 0.2>}
    }   
     rotate <0,10,0>
     translate 0.6*y
     translate 2.0*z
} //     
     

//???  object {                             //// DIELECTRIC 333  mas cerca está pedazito
//???   // Round_Box(A, B, WireRadius, Merge)
//???   Round_Box(<-1.07, 0.6, -1.15>,<-0.93, 0.3,-.4 >, 0.01, 0) 
//???  //  Round_Box(<2.5, 0.5, -0.9>,<1.15, 0.49,-1.2 >, 0.05, 0.9)
//???       texture{
//???  pigment{ color rgbt<1,0.7,0, 0.2>}
//???      }   
//???       rotate <0,10,0>
//???       translate 0.6*y
//???       translate 2.0*z
//???  } //   
               
               
//???  object {                             //// DIELECTRIC 333  mas cerca está pedazito
//???   // Round_Box(A, B, WireRadius, Merge)
//???   Round_Box(<-1.07, 0.6, -0.15>,<-0.93, 0.3,.68 >, 0.01, 0) 
//???  //  Round_Box(<2.5, 0.5, -0.9>,<1.15, 0.49,-1.2 >, 0.05, 0.)
//???       texture{
//???  pigment{ color rgbt<1,0.7,0, 0.2>}
//???      }   
//???       rotate <0,10,0>
//???       translate 0.6*y
//???       translate 2.0*z
//???  } //   
                
 
 ///////////////////////////////// ////  RESISTIVE SWITCHING MATERIAL ////////////////////////
          
object {                             ////  RESISTIVE SWITCHING MATERIAL
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1.23, 0.6, .0>,<-.83, 0.3,-0.53 >, 0.01, 0.) 
     texture{
pigment{ color rgbt<1,0,0, 0.1>}
    }   
     rotate <0,10,0>
     translate 0.6*y
     translate 2.0*z
} //     

///////////////// /// BEGIN    SOURCE ELECTRODE CONTACT   ///////////////// //////////////////// //////////////////// //////////////////// //////////////////// ///
                              
object {                    /// SOURCE ELECTRODE CONTACT 001     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.16, 0.6, 0.5>,<.36, 0.7,0.45 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 
                    
object {             /// SOURCE ELECTRODE CONTACT   002
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.16, 0.6, 0.2>,<.36, 0.7,0.15 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 
                                                                
object {             /// SOURCE ELECTRODE CONTACT   003
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.16, 0.6, -0.1>,<.36, 0.7,-0.15 >, 0.05, 0) 
//  Round_Box(<2.5, 0.5, -0.9>,<1.15, 0.49,-1.2 >, 0.05, 0)
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z} //  

object {             /// SOURCE ELECTRODE CONTACT   004
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.16, 0.6, -0.4>,<.36, 0.7,-0.45 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} //                                                                                   

object {             /// SOURCE ELECTRODE CONTACT   005
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.16, 0.6, -0.7>,<.36, 0.7,-0.75 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>      translate 0.6*y      translate 2.0*z
} // 

object {             /// SOURCE ELECTRODE CONTACT   006
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.16, 0.6, -1.>,<.36, 0.7,-1.05 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>      translate 0.6*y      translate 2.0*z
} // 
                          
                          
object {                    /// transversal   SOURCE ELECTRODE CONTACT    
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.06, 0.6, 0.5>,<1.16, 0.7,-1.05 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} //                          
                          
//////////////////////////////DRAIN/////////////////////////////////////                                              
                                              
                                              
object {                    /// DRAIN  Source to pad      
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.08, 0.6, -0.25>,<1.4, 0.7,-0.3 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 

                                                                   
object {                    /// transversal   DRAIN ELECTRODE CONTACT    
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.4, 0.6, -.55>,<1.85, 0.7,-.05 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} //            

///////////////// /// BEGIN    DRAIN ELECTRODE CONTACT     ///////////////// //////////////////// //////////////////// //////////////////// //////////////////// //////////////////// ///

object {                    /// DRAIN  ELECTRODE CONTACT 001     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1., 0.6, 0.3>,<.2, 0.7,0.35 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 
     
object {                    /// DRAIN  ELECTRODE CONTACT 002     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1., 0.6, 0.>,<.2, 0.7,0.05 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 

object {                    /// DRAIN  ELECTRODE CONTACT 003     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1., 0.6, -0.25>,<-1.05, 0.7,-0.3 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 

object {                    /// DRAIN  ELECTRODE CONTACT 004     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1., 0.6, -0.55>,<.2, 0.7,-0.6 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 

object {                    /// DRAIN  ELECTRODE CONTACT 005     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1., 0.6, -0.85>,<.2, 0.7,-0.9 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 
          
          
object {                    /// transversal   DRAIN ELECTRODE CONTACT    
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<0.22, 0.6, .37>,<0.27, 0.7,-.91 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} //                          
      

                     
//                     object {                    /// transversal   DRAIN ELECTRODE CONTACT    
// Round_Box(A, B, WireRadius, Merge)
// Round_Box(<1.2, 0.8, -0.37>,<0.27, 1,-0.12 >, 0.05, 0) 
// texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
// } //                          
      
                     
////////////////// TOP ELECTRODE   ////////////////////////////////////
      
object {                    /// DRAIN  ELECTRODE CONTACT 003     
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<-1.13, 0.6, -0.4>,<-.93, 0.7,-0.15 >, 0.05, 0) 
texture{Chrome_Metal}        rotate <0,10,0>     translate 0.6*y     translate 2.0*z
} // 

                    
//  object {                /// DRAIN Y TOP ELECTRODE CONTACT 
//  // Round_Box(A, B, WireRadius, Merge)
//  Round_Box(<-1.36, 0.6, -1.0>,<0.966, 0.7,0.35 >, 0.05, 0) 
//   //  Round_Box(<2.5, 0.5, -0.9>,<1.15, 0.49,-1.2 >, 0.05, 0)
//      texture{
//      Copper_Metal
//     }   
//      rotate <0,10,0>
//       translate 0.6*y
//      translate 2.0*z
//  } // 

     
     
     
     
     /////////////////// PENTACENE ///////////////////////////
     /////////////////// PENTACENE ///////////////////////////
     /////////////////// PENTACENE ///////////////////////////
     
     

object {                //PENTACENE
 // Round_Box(A, B, WireRadius, Merge)
 Round_Box(<1.3, 0.65, -1.2>,<0.0, 0.75,0.55 >, 0.05, 0) 
     texture{     pigment{ color rgbt<0,0,1, 0.9>} }      rotate <0,10,0>      translate 0.6*y      translate 2.0*z
} //           
