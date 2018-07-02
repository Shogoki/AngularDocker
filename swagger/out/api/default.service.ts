/**
 * Get-Servername API
 * A simple REST-API to get, add or modify Data from Get-Servername Database
 *
 * OpenAPI spec version: 1.1.0
 * Contact: de388651.evonik.onmicrosoft.com@emea.teams.ms
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
/* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs/Observable';

import { Server } from '../model/server';
import { Servers } from '../model/servers';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class DefaultService {

    protected basePath = 'http://servername-api:8080/rest';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (let consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Gets all servers
     * Returns a list containing all servers.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public serversGet(observe?: 'body', reportProgress?: boolean): Observable<Servers>;
    public serversGet(observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Servers>>;
    public serversGet(observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Servers>>;
    public serversGet(observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        let httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set("Accept", httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        let consumes: string[] = [
            'application/json'
        ];

        return this.httpClient.get<Servers>(`${this.basePath}/servers`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Adds a server
     * Adds a new server to the database, generating it´s name.
     * @param server The server to create.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public serversPost(server: Server, observe?: 'body', reportProgress?: boolean): Observable<Server>;
    public serversPost(server: Server, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Server>>;
    public serversPost(server: Server, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Server>>;
    public serversPost(server: Server, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (server === null || server === undefined) {
            throw new Error('Required parameter server was null or undefined when calling serversPost.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        let httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set("Accept", httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        let consumes: string[] = [
            'application/json'
        ];
        let httpContentTypeSelected:string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set("Content-Type", httpContentTypeSelected);
        }

        return this.httpClient.post<Server>(`${this.basePath}/servers`,
            server,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Deletes a server
     * Delete a single server identified via its id
     * @param srvid The server&#39;s id
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public serversSrvidDelete(srvid: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public serversSrvidDelete(srvid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public serversSrvidDelete(srvid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public serversSrvidDelete(srvid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (srvid === null || srvid === undefined) {
            throw new Error('Required parameter srvid was null or undefined when calling serversSrvidDelete.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        let httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set("Accept", httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        let consumes: string[] = [
            'application/json'
        ];

        return this.httpClient.delete<any>(`${this.basePath}/servers/${encodeURIComponent(String(srvid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Gets a server
     * Returns a single server for its id.
     * @param srvid The server&#39;s id
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public serversSrvidGet(srvid: number, observe?: 'body', reportProgress?: boolean): Observable<Server>;
    public serversSrvidGet(srvid: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Server>>;
    public serversSrvidGet(srvid: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Server>>;
    public serversSrvidGet(srvid: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {
        if (srvid === null || srvid === undefined) {
            throw new Error('Required parameter srvid was null or undefined when calling serversSrvidGet.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        let httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set("Accept", httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        let consumes: string[] = [
            'application/json'
        ];

        return this.httpClient.get<Server>(`${this.basePath}/servers/${encodeURIComponent(String(srvid))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
