package org.apache.maven.shared.model.fileset.mappers;

/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/**
 * Implementation of FileNameMapper that always returns the source file name.
 *
 * <p>This is the default FileNameMapper for the copy and move
 * tasks.</p>
 *
 * @version $Id: IdentityMapper.java 661727 2008-05-30 14:21:49Z bentmann $
 */
public class IdentityMapper
    implements FileNameMapper
{
    /** {@inheritDoc} */
    public void setFrom( String from )
    {
        // nop
    }

    /** {@inheritDoc} */
    public void setTo( String to )
    {
        // nop
    }

    /** {@inheritDoc} */
    public String mapFileName( String sourceFileName )
    {
        return sourceFileName;
    }
}
