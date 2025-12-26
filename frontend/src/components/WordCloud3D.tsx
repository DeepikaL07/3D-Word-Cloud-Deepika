import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Text, OrbitControls } from '@react-three/drei';
import { WordData } from '../types';
import * as THREE from 'three';

interface WordCloud3DProps {
  words: WordData[];
}

interface Word3DProps {
  word: string;
  weight: number;
  position: [number, number, number];
  color: string;
}

const Word3D: React.FC<Word3DProps> = ({ word, weight, position, color }) => {
  const meshRef = useRef<THREE.Mesh>(null);

  useFrame((state) => {
    if (meshRef.current) {
      meshRef.current.rotation.y = Math.sin(state.clock.elapsedTime * 0.3) * 0.1;
    }
  });

  const fontSize = 0.3 + weight * 0.7;

  return (
    <Text
      ref={meshRef}
      position={position}
      fontSize={fontSize}
      color={color}
      anchorX="center"
      anchorY="middle"
    >
      {word}
    </Text>
  );
};

const WordCloud3D: React.FC<WordCloud3DProps> = ({ words }) => {
  const wordElements = useMemo(() => {
    const maxWeight = Math.max(...words.map(w => w.weight));
    
    return words.map((wordData, index) => {
      const normalizedWeight = wordData.weight / maxWeight;
      
      const phi = Math.acos(-1 + (2 * index) / words.length);
      const theta = Math.sqrt(words.length * Math.PI) * phi;
      
      const radius = 8;
      const x = radius * Math.cos(theta) * Math.sin(phi);
      const y = radius * Math.sin(theta) * Math.sin(phi);
      const z = radius * Math.cos(phi);

      const hue = 200 + normalizedWeight * 160;
      const color = `hsl(${hue}, 70%, 60%)`;

      return (
        <Word3D
          key={index}
          word={wordData.word}
          weight={normalizedWeight}
          position={[x, y, z]}
          color={color}
        />
      );
    });
  }, [words]);

  return (
    <div style={{ width: '100%', height: '600px', background: '#0a0a0a' }}>
      <Canvas camera={{ position: [0, 0, 15], fov: 75 }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        {wordElements}
        <OrbitControls 
          enableZoom={true}
          enablePan={true}
          autoRotate={true}
          autoRotateSpeed={0.5}
        />
      </Canvas>
    </div>
  );
};

export default WordCloud3D;